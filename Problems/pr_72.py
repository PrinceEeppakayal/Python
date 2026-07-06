
# QUESTION: Create two virtual environments, install few packages in the first one. How do you create a similar environments in the second one?

'''# create two virtual environments:
virtualenv env1
virtualenv env2

# activate the first environment:
env1\Scripts\activate.ps1

# install few packages in the first environment:
pip install numpy pandas matplotlib

# freeze the installed packages into a requirements.txt file:
pip freeze > requirements.txt

# deactivate the first environment:
deactivate

# activate the second environment:
env2\Scripts\activate.ps1

# install the packages from the requirements.txt file into the second environment:
pip install -r requirements.txt'''