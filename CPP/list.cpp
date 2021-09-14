#include <string>
#include <iostream>
using namespace std;
/*	This laboratory work was completed in OOP model to be sure that everything works correctly
	This concept was chosen because of simple and easy-to-create version of list realisation
*/
template <typename T> // using Templates for gaining access to work with different types of data
class List {

	public:
		List(); // creation of List
		void push_back(T data); // push_back method takes templated type of data and pushes it back of the list   UPPER 2
		int GetSize() { // Public  method for granting incapsulated size of list  BASE 1
			return Size;
		}
		T& operator[](const int index); // own created operator for easy-to-access for any object of the list

	void listOut(); // Public method for output list in console.  BASE 5
	
	List<T> listCopy(List list);  // method for copying list into another UPPER 5
	
	private:
	template <typename T> // templated Nodes in list
	class Node {
	public:
		Node* pNext; // pointer for the next Node in list
		T data; // Templated data in nodes
		Node(T data = T(), Node* pNext = nullptr) { // constructor for Nodes
			this->data = data;
			this->pNext = pNext;
		}
	};
	int Size;
	Node<T>* head; // templated pointer for the head of node
};
template<typename T>
T& List<T>::operator[](const int index) 
{
	Node<T>* current = this->head;
	int counter = 0;
	while (current != nullptr) { // loopback of the list in order to find needed element
		if (counter == index) {
			return current->data;
		}
		current = current->pNext;
		counter++;
	}
}
template <typename T>
List<T> ::List() // templated method for creating list
{
	Size = 0;
	head = nullptr;
}
template<typename T>
void List<T>::push_back(T data) 
{
	if (head == nullptr) {
		head = new Node<T>(data); // creating first(head) Node in list if it's empty
	}
	else {
		Node<T>* current = this->head;
		while (current->pNext != nullptr) { // if list isn't empty we can just find last node and use it's pointer for the new_last Node
			current = current->pNext;		// whish was pushed back
		}
		current->pNext = new Node<T>(data);
	}
	Size++;
}

template<typename T>
void List<T>::listOut() // templated method for output list in console  
{
	Node<T>* current = this->head;
	cout << "List start" << endl;
	while (current != nullptr) { // output data from every Node in list
		cout << current->data << endl;
		current = current->pNext;
	}
	cout << "List end" << endl;
}

template<typename T>
List<T> List<T>::listCopy(List list) // templated method for copying list
{
	List<T> list_new;
	for (int i = 0; i < list.GetSize(); i++) {
		list_new.push_back(list[i]);
	}
	return list_new;
	cout << "List was copied. Pleae output it! " << endl;
}
