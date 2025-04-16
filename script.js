//variables
//use var
var name = "John Doe";
console.log(name); //output: John Doe

//2.let - used to declare variables that can be reassigned(modern way)
// keyword let = value;
let age = 35;
console.log(age); //output 35

//3.const - used to declare variable that cannot be re-assigned(constant value)
//keyword cont = value;
const country = "USA";
const pi = 3.14;
console.log(country); //output: USA
console.log(pi); //output: 3.14
pi = 1;
// error: Assignemnt to constant variable


//2. Number integer or float
let ageNumber = 35;
const piNumber = 3.14;

//3. String - text
let nameString = "John Doe";
let greeting = 'Hello, World!';

//4. Boolean - true or false
let isStudent = true;
let isEmployed = false;

//5. Undefined - variable that has been declared but not assigned a value
let x;
let y = undefined;

//6. Null - variable that has been assigned a null value
let z = null;

//7. Symbol - unique and immutable value
let uniqueSymbol = Symbol('unique');

// non-primitive data types - collection of values
//1. Object - collection of key-value pairs
let person = {
    name: "John Doe",
    age: 35,
    country: "USA"
};

console.log(person.name); //output: John Doe

let car = {
    make: "Toyota",
    model: "Camry",
    year: 2020
};

console.log(car.make); //output: Toyota


let colors = ["red", "green", "blue"];
console.log(colors[0]); //output: red
//2. Array - ordered collection of values

let cars = ["Toyota", "Honda", "Ford", "Chevrolet"];
console.log(cars[1]); //output: Honda

console.log(cars[4]); //output: undefined

//3. Function - reusable block of code
/*
function functionName(parameter1, parameter2) {
//code to be executed
return value;
}
*/

function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("John")); //output: Hello, John!

function greet(name, email) {
    return "Hello,my name is " + name + " and my email address is " + email;
}

console.log(greet("John", "johnbosco@gmail.com"));

//operators - symbols that perform operations on variables and values
//1. Arithmetic operators - used to perform mathematical operations
let a = 50;
let numB = 20;

let sum = a + numB; //addition
let difference = a - numB; //subtraction
let product = a * numB; //multiplication
let quotient = a / numB; //division
let remainder = a % numB; //modulus

console.log(modulus); //output: 10
console.log(sum); //output: 70
console.log(difference); //output: 30
console.log(product); //output: 1000
console.log(quotient); //output: 2.5

//2. Assignment operators - used to assign values to variables
let x = 10; //initial value
let y = 5; //reassign value
x += y; //x = x + y
console.log(x); //output: 15

//comparison operators
//used to compare values and return a boolean value
let c = 10;
let b = 20;