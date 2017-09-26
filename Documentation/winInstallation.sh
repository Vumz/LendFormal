#Step 0: Ensure that Python 3,pip, and git are installed
#Step 1: Navigate to directory to store files
#Step 2: Clone repository from github
git clone https://github.gatech.edu/sgilson7/Lend-Formal-.git
#Step 3: Install required packages
cd Lend-Formal-
cd LendFormal
pip install -r requirements.txt
#Step 4: Set up local enviornment
cd src
copy LendFormal/settings/local.sample.env Lendformal/settings/local.env
python manage.py migrate
