
import pandas
from my_lambdata.func import add_series


print("HELLO WORLD")

df = pandas.DataFrame({'odd': [1, 3, 5]})
test_list = [2, 4, 6]
df = add_series(df, test_list, 'even')
df
