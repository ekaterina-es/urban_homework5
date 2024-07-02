immutable_var = 1, 12, 95, "December", False
print("Immutable tuple:", immutable_var)

# immutable_var[1] = 24
# ~~~~~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# Кортеж является неизменяемым типом данных, таким образом, невозможно изменить его значение.

mutable_list = [1, 12, 95, "December", True]
mutable_list[1] = False
mutable_list[3] = "July"
print("Mutable list:", mutable_list)
