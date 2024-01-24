#Author: 22200727

class SymbolicExpression:
    def add(self, other):
        return Addition(self, self._convert_to_symbolic(other))

    def subtract(self, other):
        return Subtraction(self, self._convert_to_symbolic(other))

    def multiply(self, other):
        return Multiplication(self, self._convert_to_symbolic(other))

    def divide(self, other):
        return Division(self, self._convert_to_symbolic(other))

    def negate(self):
        return Negation(self)

    def _convert_to_symbolic(self, other):
        return Constant(other) if isinstance(other, (int, float)) else other

    def simplify_expr(self):
        return self

    def evaluate(self, env):
        raise NotImplementedError

    def differentiate(self, var_name):
        raise NotImplementedError

    def get_variables(self):
        raise NotImplementedError


class Constant(SymbolicExpression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def evaluate(self, env):
        return self

    def differentiate(self, var_name):
        return Constant(0)

    def get_variables(self):
        return []


class Variable(SymbolicExpression):
    def __init__(self, var_name):
        self.var_name = var_name

    def __str__(self):
        return self.var_name

    def evaluate(self, env):
        return Constant(env.get(self.var_name, 0))

    def differentiate(self, var_name):
        return Constant(1 if self.var_name == var_name else 0)

    def get_variables(self):
        return [self.var_name]


class BinaryOperation(SymbolicExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.op_symbol} {self.right})"

    def evaluate(self, env):
        return self.operation(self.left.evaluate(env).value, self.right.evaluate(env).value)

    def get_variables(self):
        return self.left.get_variables() + self.right.get_variables()


class Addition(BinaryOperation):
    op_symbol = "+"

    def operation(self, x, y):
        return Constant(x + y)

    def differentiate(self, var_name):
        return self.left.differentiate(var_name).add(self.right.differentiate(var_name))


class Subtraction(BinaryOperation):
    op_symbol = "-"

    def operation(self, x, y):
        return Constant(x - y)

    def differentiate(self, var_name):
        return self.left.differentiate(var_name).subtract(self.right.differentiate(var_name))


class Multiplication(BinaryOperation):
    op_symbol = "*"

    def operation(self, x, y):
        return Constant(x * y)

    def differentiate(self, var_name):
        return (self.left.differentiate(var_name).multiply(self.right)
                .add(self.left.multiply(self.right.differentiate(var_name))))


class Division(BinaryOperation):
    op_symbol = "/"

    def operation(self, x, y):
        if y == 0:
            raise ValueError("Division by zero")
        return Constant(x / y)

    def differentiate(self, var_name):
        numerator = (self.left.differentiate(var_name).multiply(self.right)
                     .subtract(self.left.multiply(self.right.differentiate(var_name))))
        denominator = self.right.multiply(self.right)
        return Division(numerator, denominator)


class Negation(SymbolicExpression):
    def __init__(self, operand):
        self.operand = operand

    def __str__(self):
        return f"(-{self.operand})"

    def evaluate(self, env):
        return Constant(-self.operand.evaluate(env).value)

    def differentiate(self, var_name):
        return self.operand.differentiate(var_name).negate()

    def simplify_expr(self):
        simplified_operand = self.operand.simplify_expr()
        if isinstance(simplified_operand, Constant):
            return Constant(-simplified_operand.value)
        return Negation(simplified_operand)


# Example usage
x = Variable("x")
expr1 = Constant(1).divide(x.add(Constant(1)))
expr2 = x.subtract(x.negate()).divide(x.add(x.negate()))

print("Expression 1:", expr1)
print("Expression 2:", expr2)

simplified_expr1 = expr1.simplify_expr()
simplified_expr2 = expr2.simplify_expr()

print("Simplified Expression 1:", simplified_expr1)
print("Simplified Expression 2:", simplified_expr2)

evaluation_env = {"x": 2}
print("Evaluated Simplified Expression 1:", simplified_expr1.evaluate(evaluation_env))

evaluation_env = {"x": 1}
print("Evaluated Simplified Expression 2:", simplified_expr2.evaluate(evaluation_env))
