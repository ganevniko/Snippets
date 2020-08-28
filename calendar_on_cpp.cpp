
#include <iostream>
#include <cmath>

using namespace std;

int printMonthCalender(int numOfDays, int startingDay);
bool leapYear( int year);
void printYearCalender(int year, int startingDay);

int main() {
    int n, firstDay;
    cout<<"Please enter the year:";
    cin>>n;
    cout<<"What day of the week was January 1st, for example enter 2 for Tuesday:";
    cin>>firstDay;
    printYearCalender(n, firstDay);
    return 0;
}

int printMonthCalender(int numOfDays, int startingDay){
    int numberOfSpaces, dayNumber=1;

    cout<<"Mon\tTue\tWed\tThr\tFri\tSat\tSun"<<endl;
    numberOfSpaces=startingDay;
    for (int i = 0; i <= numberOfSpaces - 2; i++)
        cout << "\t";
    while (dayNumber <= numOfDays) {
        cout << dayNumber<<"\t";
        dayNumber++;
        numberOfSpaces++;
        if (numberOfSpaces == 8){
            numberOfSpaces =1;
            cout<<endl;
        }


    }
    return numberOfSpaces-1;
}

bool leapYear( int year){
    if (year%4==0 && year%100!=0)  {
        return true;
    }
    else if (year%400==0) {
        return true;
    }
    else
        return false;
}

void printYearCalender(int year, int startingDay){
    int lastDay;
    cout<<"January "<<year<<endl;
    lastDay=printMonthCalender(31,startingDay)+1;
    cout<<endl<<endl;

    if (leapYear(year)) {
        cout << "February " << year << endl;
        lastDay = printMonthCalender(29, lastDay)+1;
        cout<<endl<<endl;
    }
    else {
        cout << "February " << year << endl;
        lastDay = printMonthCalender(28, lastDay)+1;
        cout<<endl<<endl;

    }

    cout<<"March "<<year<<endl;
    lastDay=printMonthCalender(31,lastDay)+1;
    cout<<endl<<endl;

    cout<<"April "<<year<<endl;
    lastDay=printMonthCalender(30,lastDay)+1;
    cout<<endl<<endl;

    cout<<"May "<<year<<endl;
    lastDay=printMonthCalender(31,lastDay)+1;
    cout<<endl<<endl;

    cout<<"June "<<year<<endl;
    lastDay=printMonthCalender(30,lastDay)+1;
    cout<<endl<<endl;

    cout<<"July "<<year<<endl;
    lastDay=printMonthCalender(31,lastDay)+1;
    cout<<endl<<endl;

    cout<<"August "<<year<<endl;
    lastDay=printMonthCalender(31,lastDay)+1;
    cout<<endl<<endl;

    cout<<"September "<<year<<endl;
    lastDay=printMonthCalender(30,lastDay)+1;
    cout<<endl<<endl;

    cout<<"October "<<year<<endl;
    lastDay=printMonthCalender(31,lastDay)+1;
    cout<<endl<<endl;

    cout<<"November "<<year<<endl;
    lastDay=printMonthCalender(30,lastDay)+1;
    cout<<endl<<endl;

    cout<<"December "<<year<<endl;
    lastDay=printMonthCalender(31,lastDay)+1;
    cout<<endl<<endl;
}
