# virtual wallet with admin and multi user login with interchangeble amounts-in-python

# Virtual Wallet
# This is a virtual wallet built using Django and Django Rest Framework.

# Installation
# Clone the repository to your local machine:

git clone https://github.com/btmstage3/virtual-wallet-with-admin-and-multi-user-login-with-interchangeble-amounts-in-python.git

# Install the required dependencies:

pip install -r requirements.txt

# Create a virtual environment (optional but recommended):

python3 -m venv env

# Activate the virtual environment:
# On Windows:

env\Scripts\activate

# On Unix or Linux:

source env/bin/activate

# Run the migrations:

python manage.py migrate

# Create a superuser:

python manage.py createsuperuser

# Run the server:

python manage.py runserver

# Open your web browser and go to http://localhost:8000 to see the project.


# Functionality
 User can register and sign in to the wallet.
 There are two types of users - premium and non-premium. This is chosen at the time of sign up.
 When someone signs up as a premium user, INR 2,500 is credited to their wallet automatically. And if the sign up is non-premium then INR 1,000 is credited to the user's wallet.
Users can send and receive money to and from other users, except the superuser.
 Sending Money - Sender (Any user) can select any other user and send money to him/her. Both Sender and receiver will pay charges for the transaction as per Table 1. The transaction charges debited from the users will be credited to the Super Users wallet.
 Requesting Money - Requester (Any user) can select any other user and request money from him/her. The user receiving the request will have the option to accept or deny the request. If the request receiver accepts, both sender and receiver will pay charges for the transaction as per Table 1. The transaction charges will be credited to the Super Users wallet.
 Each User can see their wallet balance.
 Each User can see all their transactions.
 Each User can see all the Money requests, action, and status.


# Superuser Commands
# The superuser can use the following commands:

 python manage.py create_premium_user <username> - Creates a premium user with the given username and credits INR 2,500 to their wallet.
 python manage.py create_non_premium_user <username> - Creates a non-premium user with the given username and credits INR 1,000 to their wallet.
 python manage.py recharge_wallet <username> <amount> - Credits the given amount to the user's wallet.
 python manage.py debit_wallet <username> <amount> - Debits the given amount from the user's wallet.
 python manage.py change_user_type <username> <type> - Changes the type of the user (premium or non-premium).


# License
 This project is licensed under the MIT License - see the LICENSE.md file for details.
