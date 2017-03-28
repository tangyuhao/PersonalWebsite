Most people who have learnt computer programming know C/C++. As a relative of C, C++ has very similar syntax but more powerful features. This article mainly talks about some different parts of C++ and C with some basic syntax.
## The difference of C and C++
C is a procedural programming language thus does not support classes and objects while C++ is a combination of procedural and object oriented programming language(OOP). In a word, you can regard C++ as a hybrid language of C.
If you are a C fan but did not use C++ in the past, you can simply change you file extension to `.cpp` and use g++ to compile it. C++ is completely compatible with C.

```bash
$ g++ -o <output_name> <sourcefile_name>.cpp
```

**Note:** `.C`, `.cc`, `.cpp`, `.c++`, `.cp`, or `.cxx` are all C++ source files suffixes; header files have suffixes like: `.h`, `.hpp`, `.hh`. The reason why C++ has so many suffixes is just about conventions. Most commonly used suffixes are `.cpp` and `.hpp`.

## basic syntax
In this part, I only talk about some important syntax which is different from C, if you would like more details please refer to C++ reference documents or textbooks like "C++ primer".
### hello world
The hello world C++ file example is:

```cpp
#include <iostream> // standard library that provides IO
int main()
{
    // std is namespace of C++ standard library
    // namespace uses '::' as scope operator
    // cout is to print to standard output
    // endl is just like '\n'
    std::cout<<"Hello world!"<<std::endl;
    return 0;
}
```
**Note:** Namespace is the mechanism for putting names defined by a library into a single place. Namespaces help avoid inadvertent name clashes. The names defined by the C++ library are in the namespace `std`.

### class
In C++ we use classes to define our own data types. A class defines a type along with a collection of operations that are related to that type. The class mechanism is one of the most important features in C++. In fact, a primary focus of the design of C++ is to make it possible to define class types that behave as naturally as the built-in types.

Here is an example of a class of Complex number.

```cpp
class Complex {
    private:
        float real, imag;
    public:
        Complex(){ // default constructor
            real = 0;// real is the member of ComplexNumber
            imag = 0;
        }
        Complex(double real, double imag){ // constructor
            this->real = real;// need to use this-> to tell compiler that you mean the member "real" of this object
            this->imag = imag;
        }
        Complex(const Complex &c){ // this is copy constructor
            real = c.real;
            imag = c.imag;
        }
        Complex add(const Complex &input1, const Complex &input2);
        Complex operator+(const Complex &c2){
            return Complex(real+c2.real, imag+c2.imag);
        }
        bool operator==(const Complex &c2){
            if (real == c2.real && imag == c2.imag)
                return true;
            else
                return false;
        }
        void print(){
            cout<<real<<"+"<<imag<<"j"<<endl;
        }
        ~Complex(void){} // destructor
};
Complex Complex::add(const Complex &input1, const Complex &input2){
    return Complex(input1.real + input2.real, input1.imag + input2.imag);
}

int main(){
    Complex a(1,2); // initialize a to be 1 + 2j
    a = a + Complex(2,3); // add a by 2 + 3j
    a.print(); // output: 3 + 5j
    return 0;
}
```

### dynamic memory allocation
In C, we usually use `malloc`, `calloc` to allocate memory. However, in C++, we have `new` stead.

```cpp
// *********** C syntax ***********
Complex *S2;
S2 = (Complex *)malloc(sizeof(Complex));
char *s;
s = (char *)malloc(sizeof(char)*3);
int *p;
p = (int *)malloc(sizeof(int));
*p = 10;
/* initialize a 2D array */
int ** ary = (int **)malloc(sizeof(int *) * rowCount);
int i;
for (i = 0; i < rowCount; ++i)
    ary[i] = (int *)malloc(sizeof(int) * colCount);
    
// *********** C++ syntax ***********
Complex *S2;
S2 = new Complex;
char *s;
s = new char[3];
int *p;
p = new int(10);// allocate and initialize
/* initialize a 2D array */
int** ary = new int*[rowCount];
for(int i = 0; i < rowCount; ++i)
    ary[i] = new int[colCount];
```

### const
we use `const` to define constant in C++. For example:

```cpp
const int M = 20; // constant M is an int
const int *p; // or int const *p, means p is variable, but *p is a constant
const * int p; // p is constant, *p is a variable
```

### function template
Say that you want to define a function to sway two variables, you may find writing similar functions for different types annoying. C++ has provided you a new feature called template thus you can write a function once for all types. Here is the example:
**swapping:**

```cpp
template <typename SWAP> 
void swap(SWAP &x, SWAP &y) {
    SWAP t;
    t = x;
    x = y;
    y = t;}
// use this function template
int a = 3, b = 5;
swap(a,b);
// now a is 5, b is 3
```


## use C and C++ together
In most cases, you can use C syntax in C++ files, but sometimes you will find some errors. This might be solve by adding:

```cpp
extern C {
// your C code
}
```
Your can refer to this link to find out: [In C++ source, what is the effect of extern “C”?](http://stackoverflow.com/questions/1041866/in-c-source-what-is-the-effect-of-extern-c)

## use C and C++ together
### use C and C++ together

### use C and C++ together
## use C and C++ together
## use C and C++ together








