#include "list.cpp"

using namespace std;

int main()
{
	int number = 1;
	List<int> list;

	cout << "Please, enter number. You can continue, while number not 0" << endl << endl;
	while (number != 0) {
		cin >> number;
		list.push_back(number);
	}

	cout << "You ended your list. Here it is" << endl << endl;
	list.listOut();

	cout << "The length of list is" << list.GetSize() << endl << endl;

	cout << "Here is copy of the last list" << endl << endl;
	List<int>copied_list;
	copied_list.listCopy(list);
	cout << endl << endl;

	string str;
	List<string> lst;
	cout << "Created new list" << endl << endl;
	while (str != "0") {
		lst.push_back(str);
		cin >> str;
	}

	cout << "You ended your list. Here it is" << endl << endl;
	lst.listOut();

	return 0;

}
