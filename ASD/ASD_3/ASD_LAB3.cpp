#include <string>
#include <iostream>
#include <sstream>
using namespace std;
//*--------------------------------------------------- ARRAY-BASED TYPE OF WORK----------------------------------------------*
class string_arr {										//array-based class of list
	string* str;										
	size_t size;
public:
	string_arr() { str = NULL; size = 0; };				//deafult constructor
	~string_arr() { delete[] str; }						//default deconstructor
	string_arr(size_t i) { size = i; str = new string[size]; }

	void main_task();

	string& operator[](const int index);
	friend istream& operator>>(istream& stream, string_arr& list);
	friend ostream& operator<<(ostream& stream, const string_arr& list);

};
string& string_arr::operator[](const int index)			//overloaded opertor for easy-to-access to array
{
	return str[index];
}
ostream& operator<<(ostream& stream, const string_arr& list)
{
	if (list.str != NULL) {								//overloaded operator for output
		for (size_t i = 0; i < list.size; i++) {
			stream << list.str[i] << " ";
		}
	}
	return stream;
}
istream& operator>>(istream& stream, string_arr& list)	//overloaded operator for input
{
	string input;
	getline(cin, input, '.');
	string buf;

	stringstream ss;
	ss << input;
	ss >> list.size;

	list.str = new string[list.size];
	for (size_t i = 0; i < list.size; ++i) {
		if (!ss.eof())
		{
			ss >> buf;
			ss.ignore(1);
			list.str[i] = buf;
		}
		else
			break;
	}
	return stream;
}
void string_arr::main_task()							// main task of laboratory work, IV variant
{
	string first = this->str[0];						// first element is pivot to comparasion
	cout << first << " ";								// console out it
	try {
		this->size <2 ? throw 4 : NULL;;				// if list has less then 2 elements - throw error
		for (size_t i = 1; i < this->size; i++) {
			string current = this->str[i];				// in this loop we select i element of list and check if it's same as the first
			if (current != first) {
				if (current.size() % 2 == 0) {			// if it isn't same and it's length is doubled - we double the first letter of the word (of the selected element)
					cout << current.insert(0, 1, current[0]) << " ";
				}
				else {
					current.erase(current.end() - 1);;	//if it's length isn't doubled - we just delete the last letter of the word
					cout << current << " ";
				}
			}
		}
	}
	catch (int i) {
		cout << "Error" << i << " Less then 2 words present";
	}

}


//*--------------------------------------------------- LIST-BASED TYPE OF WORK-----------------------------------------------------------*
class Node {
public:
	Node* pNext;										// pointer for the next Node in list
	Node* pPrev;										// pointer for the prev Node in list
	string data;										//  data in nodes
	Node() {											// constructor for Nodes
		this->data = "";
		this->pPrev = nullptr;
		this->pNext = nullptr;

	}
};
class List {
	Node* head = nullptr, * tail = nullptr;				//  pointers for the head and tail of list
	int Size;
public:
	List();												// creation of List
	void listOut();										// Public method for output list in console. 
	void insert(string data);
	int GetSize() { return Size; }
	void main_task();

	string& operator[](const int index);				// own created operator for easy-to-access for any object of the list
	friend ostream& operator<<(ostream& stream, const List& mylist);
	friend istream& operator>>(istream& stream, List& list);

};
void List::main_task()									// main task of laboratory work, IV variant
{
	string first = this->operator[](0);					// first element is pivot to comparasion
	cout << first << " ";								// console out it
	try {
		this->GetSize() <2 ? throw 4 : NULL;			// if list has less then 2 elements - throw error
		for (int i = 0; i < this->GetSize(); i++) {	
			string current = this->operator[](i);		// in this loop we select i element of list and check if it's same as the first
			if (current != first) {
				if (current.size() % 2 == 0) {			// if it isn't same and it's length is doubled - we double the first letter of the word (of the selected element)
					cout << current.insert(0, 1, current[0]) << " ";
				}
				else {
					current.erase(current.end() - 1);	//if it's length isn't doubled - we just delete the last letter of the word
					cout << current << " ";
				}
			}
		}
	}
	catch (int i) {
		cout << "Error" << i << " Less then 2 words present";
	}
	
}
void List::insert(string data) {
	Node* temp = new Node;								//creating new Node
	temp->pNext = NULL;                   
	temp->data = data;                        

	if (this->head != NULL)								//check for empty list     
	{
		temp->pPrev = tail;								//adding new Node to the end of the list causes that new element have to have the tail pointer as the tail itselft
		tail->pNext = temp;               
		tail = temp;									//changing of the tail to be the last element in list
		this->Size++;
	}
	else												//if the list is empty
	{
		temp->pPrev = NULL;								//the Prev pointer is in null
		head = tail = temp;								// the only one node is the head and the tail of the while list
		this->Size++;
	}
}
string& List::operator[](const int index)
{
	Node* current = this->head;
	int counter = 0;
	while (current != nullptr) {						// loopback of the list in order to find needed element
		if (counter == index) {
			return current->data;
		}
		current = current->pNext;
		counter++;
	}
}

List ::List()											//  method for creating list
{
	head = nullptr;
	tail = nullptr;
	Size = 0;
}


void List::listOut()									//  method for output list in console  
{
	Node* current = this->head;
	cout << "List start" << endl;
	while (current != nullptr) {						// output data from every Node in list
		cout << current->data << endl;
		current = current->pNext;
	}
	cout << "List end" << endl;
}
ostream& operator<<(std::ostream& stream, const List& list) {

	if (list.head != NULL) {							// overloaded operator for output
		Node* temp = list.head;
		while (temp != nullptr)
		{
			stream << temp->data << " ";
			temp = temp->pNext;
		}
	}
	return stream;
}
std::istream& operator>>(std::istream& stream, List& list) {
	string input;										// overloaded operator for input
	getline(cin, input, '.');

	stringstream ss;
	ss << input;
	string buf;
	while (!ss.eof())
	{
		ss >> buf;
		ss.ignore(1);
		list.insert(buf);
}

	return stream;
}

int main() {
	//testing for string_arr
#if 0
	string_arr arr;
	cin >> arr;
	//cout << arr;
	arr.main_task();
#endif
	List newlist;
	cin >> newlist;
	cout << endl;
	cout << newlist << endl;
	newlist.main_task();
	cout << endl << endl << endl;


}
