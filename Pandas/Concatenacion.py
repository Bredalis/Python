
import pandas as pd

Left = pd.DataFrame({

	'Key': range(5),
	'Left_Value': [1, 2, 3, 4, 5]
})

Right = pd.DataFrame({

	'Key': range(2, 7),
	'Right_Value': [1, 2, 3, 4, 5]
})

# Concatenacion Vertical
# Horizontal

print(pd.concat([Left, Right]))
print(pd.concat([Left, Right], axis = 1))

print(pd.merge(Left, Right, on = 'Key'))