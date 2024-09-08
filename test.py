import pickle
with open('SIH_final_database_reworked.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Test the loaded model
result = loaded_model.predict([[7,9,10,2,3,4,5]])
print(result)