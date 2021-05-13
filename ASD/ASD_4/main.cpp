#include <iostream>
#include <queue>
#include <stack>

void queue(){
    std::queue<char> queue;

    std::cout << "- Add 27 letters: \n";
    for (int i = 0; i < 27; i++) {
        queue.push((char) ('a' + i));
    }

    std::cout << "- Poll 17 elements: \n";
    for (int i = 0; i < 17; i++) {
        std::cout << queue.front() << '\n';
        queue.pop();
    }

    std::queue<int> queue2;

    queue2.push(12);
    queue2.push(75);

    queue2.back() -= queue2.front();

    std::cout << "queue.back() is now " << queue2.back() << '\n';

}

void stack(){
    std::stack<char> stack;

    std::cout << "- Add 27 letters: \n";
    for (int i = 0; i < 27; i++) {
        stack.push((char) ('a' + i));
    }

    std::cout << "- Poll 17 elements: \n";
    for (int i = 0; i < 17; i++) {
        std::cout << stack.top() << '\n';
        stack.pop();
    }


}

int main() {
    queue();
    stack();
    return 0;
}
