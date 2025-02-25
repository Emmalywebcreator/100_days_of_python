from prettytable import PrettyTable, TableStyle

table = PrettyTable()

# print(table)

table.add_column("State", ["Delta", "Edo", "Lagos", "Rivers", "Bayelsa"], "l")
table.add_column("Capital", ["Asaba", "Benin City", "Ikeja", "Portharcourt", "Yenagua"], "l")
table.add_row(["Oyo", "Ibandan"], divider=True)

print("Table 1")
print(table)
print("\n")
table2 = PrettyTable()
table2.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table2.add_row(["Adelaide", 1295, 1158259, 600.5])
table2.add_divider()
table2.add_row(["Brisbane", 5905, 1857594, 1146.4])
table2.add_row(["Darwin", 112, 120900, 1714.7])
table2.add_row(["Hobart", 1357, 205556, 619.5], divider=True)
table2.add_row(["Melbourne", 1566, 3806092, 646.9])
table2.add_row(["Perth", 5386, 1554769, 869.4])
table2.add_row(["Sydney", 2058, 4336374, 1214.8])

print("Table2")
print(table2)
print("\n")


table3 = PrettyTable()
table3.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table3.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ],
)

print("Table 3")
print(table3)