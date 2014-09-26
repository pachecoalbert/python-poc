formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter %  (
    "I had this thing.",
    "that you could tyope up right.",
    "But it din't sing.",
    "so I said goodnight."
)
