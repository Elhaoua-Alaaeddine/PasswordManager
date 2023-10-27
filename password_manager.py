class PasswordManager:
    def __init__(self):
        self.password_file = None
        self.password_dict = {}

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(self.password_file, 'r') as f:
            for line in f:
                site, password = line.split(':')
                self.password_dict[site] = password

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                f.write(site + ': ' + password + '\n')

    def get_password(self, site):
        return self.password_dict[site]



def main():
    print('Welcome to Password Manager!')
    password = {
        'Website/App': 'Password'
    }

    pm = PasswordManager()

    print("""What do you want to do?
            (1) Create a new password file
            (2) Load a password file
            (3) Add a new password
            (4) Get a password
            (5) Exit
        """)

    done = False
    while not done:
        choice = input('Enter your choice: ')
        match choice:

            case '1':
                path = input('Enter the path to store the password file: ')
                pm.create_password_file(path, password)

            case '2':
                path = input('Enter the path to the password file: ')
                pm.load_password_file(path)

            case '3':
                site = input('Enter the site: ')
                password = input('Enter the password: ')
                pm.add_password(site, password)

            case '4':
                site = input('Enter the site: ')
                print('the password of the site ',site, ':', pm.get_password(site))

            case '5':
                done = True

            case _:
                print('Invalid choice')


if __name__ == '__main__':
    main()
