import math

def maxGameScore(cell):
    score = 0
    current_cell = 0

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True  

    def nextPrime(start):
        num = start
        while True:
            num += 1
            if is_prime(num) and '3' in str(num):
                return num

    for c in cell:
        if current_cell + c >= len(cell):
            score += sum(cell[current_cell:])
            break
        move = nextPrime(current_cell)
        choice = 'R' if move > 1 else '1'
        current_cell += move
        score += cell[current_cell]
    return score

if __name__ == '__main__':
    cells = [int(x) for x in input().split()]
    result = maxGameScore(cells)
    print(result)













import math

def maxGameScore(cell):
    score = 0
    current_cell = 0

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return 
    def find_next_prime_with_digit_3(start):
        num = start
        while True:
            num += 1
            if is_prime(num) and '3' in str(num):
                return num
    for c in cell:
        if current_cell + c >= len(cell):
            score += sum(cell[current_cell:])
            break
        move = find_next_prime_with_digit_3(current_cell)
        choice = 'R' if move > 1 else '1'
        current_cell += move
        score += cell[current_cell]
    return score

if __name__ == '__main__':
    #num = int(input("How many cells are there? "))
    cells = []
    for i in range(num):
        cell_val = int(input("Enter the values of the cells: "))
        cells.append(cell_val)
    result = maxGameScore(cells)





#include <bits/stdc++.h>
using namespace std;
#include <iostream>
#include <string>
#include <unordered_map>

int mapStringToVals(const string& str) {
    unordered_map<string, int> strToVals = {
        {"a", 1}, {"b", 1},
        {"c", 2}, {"d", 2}, {"e", 2},
        {"f", 3}, {"g", 3}, {"h", 3},
        {"i", 4}, {"j", 4}, {"k", 4},
        {"l", 5}, {"m", 5}, {"n", 5},
        {"o", 6}, {"p", 6}, {"q", 6},
        {"r", 7}, {"s", 7}, {"t", 7},
        {"u", 8}, {"v", 8}, {"w", 8},
        {"x", 9}, {"y", 9}, {"z", 9}
    };

    return strToVals[str];
}

int countSubstrings(const string& input_str) {
    int count = 0;
    int length = input_str.length();

    for (int i = 0; i < length; i++) {
        int sum = 0;
        for (int j = i; j < length; j++) {
            sum += mapStringToVals(string(1, input_str[j]));
            if (sum % (j - i + 1) == 0) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    string input;
    getline(cin, input);
    int result = countSubstrings(input);
    cout << result << endl;

    return 0;
}



#include <bits/stdc++.h>
#include <jsoncpp/json/json.h>
#include <jsoncpp/json/reader.h>
#include <jsoncpp/json/writer.h>
#include <jsoncpp/json/value.h>
#include <curl/curl.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'healthCheckup' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER lowerlimit
 *  2. INTEGER upperlimit
 * API URL: https://jsonmock.hackerrank.com/api/medical_records?page={page_no}
 */

int healthCheckup(int lowerlimit, int upperlimit) {

}

int main()



def healthCheckup(lowerlimit, upperlimit):
    page_number = 1
    total_fit_records = 0

    while True:
        url = f"https://jsonmock.hackerrank.com/api/medical_records?page={page_number}"
        try:
            response = requests.get(url)
            response.raise_for_status()  

            data = response.json()
            if page_number > data.get('total_pages', 0):
                break

            for record in data.get('data', []):
                score = record.get('score', None)
                if score is not None and lowerlimit <= score <= upperlimit:
                    total_fit_records += 1

            page_number += 1
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    return total_fit_records
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lowerlimit = int(input().strip())

    upperlimit = int(input().strip())

    result = healthCheckup(lowerlimit, upperlimit)

    fptr.write(str(result) + '\n')

    fptr.close()




def healthCheckup(lowerlimit, upperlimit):
    page_number = 1
    total_fit_records = 0

    while True:
        url = f"https://jsonmock.hackerrank.com/api/medical_records?page=   {page_number}"
        response = requests.get(url)
        data = response.json()

        if page_number > data['total_pages']:
            break

        for record in data['data']:
            score = record['score']

            if lowerlimit <= score <= upperlimit:
                total_fit_records += 1
        page_number += 1

    return total_fit_records

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lowerlimit = int(input().strip())

    upperlimit = int(input().strip())

    result = healthCheckup(lowerlimit, upperlimit)

    fptr.write(str(result) + '\n')

    fptr.close()



import math

def maxGameScore(cell):
    score = 0
    current_cell = 0

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True  # Fixed the return statement

    def find_next_prime_with_digit_3(start):
        num = start
        while True:
            num += 1
            if is_prime(num) and '3' in str(num):
                return num

    for c in cell:
        if current_cell + c >= len(cell):
            score += sum(cell[current_cell:])
            break
        move = find_next_prime_with_digit_3(current_cell)
        choice = 'R' if move > 1 else '1'
        current_cell += move
        score += cell[current_cell]
    return score

if __name__ == '__main__':
    num = int(input("How many cells are there? "))  # Uncomment this line to get the number of cells
    cells = []
    for i in range(num):
        cell_val = int(input("Enter the values of the cells: "))
        cells.append(cell_val)
    result = maxGameScore(cells)
    print("Result:", result)