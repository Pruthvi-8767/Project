import requests

class Covid19API:
    def __init__(self):
        self.base_url = "https://disease.sh/v3/covid-19"

    def get_global_data(self):
        url = f"{self.base_url}/all"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_country_data(self, country):
        url = f"{self.base_url}/countries/{country}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_data_by_date(self, country, date):
        url = f"{self.base_url}/historical/{country}?lastdays=30"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if date in data['timeline']['cases']:
                return {
                    'cases': data['timeline']['cases'][date],
                    'deaths': data['timeline']['deaths'][date],
                    'recovered': data['timeline']['recovered'][date]
                }
            else:
                return None
        else:
            return None


class Covid19Menu:
    def __init__(self):
        self.api = Covid19API()

    def display_global_stats(self):
        data = self.api.get_global_data()
        if data:
            print("\nGlobal COVID-19 Statistics:")
            print(f"Total Cases: {data['cases']}")
            print(f"Total Deaths: {data['deaths']}")
            print(f"Total Recovered: {data['recovered']}")
        else:
            print("Error: Unable to fetch global data.")

    def display_country_stats(self, country):
        data = self.api.get_country_data(country)
        if data:
            print(f"\nCOVID-19 Statistics for {country.capitalize()}:")
            print(f"Total Cases: {data['cases']}")
            print(f"Total Deaths: {data['deaths']}")
            print(f"Total Recovered: {data['recovered']}")
        else:
            print(f"Error: Unable to fetch data for {country.capitalize()}.")

    def display_data_by_date(self, country, date):
        data = self.api.get_data_by_date(country, date)
        if data:
            print(f"\nCOVID-19 Data for {country.capitalize()} on {date}:")
            print(f"Cases: {data['cases']}")
            print(f"Deaths: {data['deaths']}")
            print(f"Recovered: {data['recovered']}")
        else:
            print(f"Error: Unable to fetch data for {country.capitalize()} on {date}.")

    def main_menu(self):
        while True:
            print("\nCOVID-19 Patient Record System")
            print("1. Display Global COVID-19 Statistics")
            print("2. Display COVID-19 Statistics for a Country")
            print("3. Display COVID-19 Data by Date for a Country")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.display_global_stats()
            elif choice == '2':
                country = input("Enter the country name (e.g., India, USA, etc.): ").lower()
                self.display_country_stats(country)
            elif choice == '3':
                country = input("Enter the country name (e.g., India, USA, etc.): ").lower()
                date = input("Enter the date (format: MM/DD/YYYY): ")
                self.display_data_by_date(country, date)
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")


# Main function to run the project
if __name__ == '__main__':
    menu = Covid19Menu()
    menu.main_menu()
