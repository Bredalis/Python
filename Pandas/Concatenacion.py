
import pandas as pd

left_frame = pd.DataFrame({

	'Key': range(5),
	'Left_Value': [1, 2, 3, 4, 5]
})

right_frame = pd.DataFrame({

	'Key': range(2, 7),
	'Right_Value': [1, 2, 3, 4, 5]
})

# Concatenacion Vertical
# Horizontal

print(pd.concat([left_frame, right_frame]))
print(pd.concat([left_frame, right_frame], axis = 1))

print(pd.merge(left_frame, right_frame, on = 'Key'))