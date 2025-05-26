const max = 1000;   // Set upper bounds
const min = 0;      // Set lower bounds
let check4prime;    // Global object, created once at page load

class Check4Prime {
    constructor() {
        this.primeBucket = new Array(max + 1).fill(true);
        this.generatePrimes();
    }

    // Generates all prime numbers up to max using Sieve of Eratosthenes
    generatePrimes() {
        this.primeBucket[0] = false;
        this.primeBucket[1] = false;

        const limit = Math.floor(Math.sqrt(max));

        for (let i = 2; i <= limit; i++) {
            if (this.primeBucket[i]) {
                for (let j = i * i; j <= max; j += i) {
                    this.primeBucket[j] = false;
                }
            }
        }
    }

    // Check if number is prime based on precomputed array
    primeCheck(num) {
        return this.primeBucket[num] === true;
    }

    // Validate input argument for prime check
    checkArgs() {
        if (arguments.length !== 1) {
            throw new Error("Exactly one argument is required.");
        }
    
        const input = arguments[0];
    
        if (input === undefined) throw new Error("Input is undefined.");
        if (input === "") throw new Error("Input is empty.");
    
        const parsed = parseFloat(input);  // Attempt to parse as a float
        if (isNaN(parsed)) throw new Error("Input is not a valid number.");
    
        // Check if the parsed value is an integer
        if (!Number.isInteger(parsed)) throw new Error("Input is not an integer."); // Rejects floats
    
        if (parsed < min) throw new Error("Input is below minimum allowed.");
        if (parsed > max) throw new Error("Input is above maximum allowed.");
    }
    
}

// Run once at page load – initializes prime data for whole session
function initializePrimes() {
    check4prime = new Check4Prime();
    checkTest(); // Kör testerna en gång vid sidladdning och kommenteras annars ut.
}

/*
Used when user checks number manually via input field
*/
function check(num) {
    try {
        check4prime.checkArgs(num);  // Validate user input (no pre-parsing!)
        alert(`Is number ${num} a prime? ${check4prime.primeCheck(num)}`);
        assert(true, `Input/number: ${num} – valid check`);
    } catch (err) {
        alert(`Error: ${err.message}`);
        let description = `Input/number: ${num}. Error in checkArgs(): ${err.message}`;
        assert(true, description);  // Visar att fel hanterades korrekt
    }
}

/*
Append test result to list on web page
*/
function assert(outcome, description) {
    let output = document.querySelector('#output');
    let li = document.createElement('li');
    li.className = outcome ? 'pass' : 'fail';
    li.appendChild(document.createTextNode(description));
    output.appendChild(li);
}

/*
Used by test cases to check input that should throw errors
*/
function assertThrowsInput(value, description) {
    try {
        check4prime.checkArgs(value);
        assert(false, description);
    } catch (err) {
        assert(true, description);
    }
}

/*
Run all unit tests
*/
function checkTest() {
    test_Check4Prime_known_true();
    test_Check4Prime_known_false();
    test_Check4Prime_checkArgs_neg_input();
    test_Check4Prime_checkArgs_above_upper_bound();
    test_Check4Prime_checkArgs_char_input();
    test_Check4Prime_checkArgs_2_inputs();
    test_Check4Prime_checkArgs_empty_input();
    test_Check4Prime_checkArgs_undefined_input();
    test_Check4Prime_checkArgs_non_integer_input();
    test_Check4Prime_valid_zero_input(); // 0 är giltigt, men inte ett primtal
}

/* === TEST CASES BELOW === */

function test_Check4Prime_known_true() {
    let knownTrue = [3, 17, 29, 997];
    for (let num of knownTrue) {
        assert(check4prime.primeCheck(num), `Test for known true primes with: ${num}`);
    }
}

function test_Check4Prime_known_false() {
    let knownFalse = [0, 1, 4, 6, 8, 9, 10, 12, 15, 21, 100, 200, 999];
    for (let num of knownFalse) {
        assert(!check4prime.primeCheck(num), `Test for known false primes with: ${num}`);
    }
}

function test_Check4Prime_checkArgs_neg_input() {
    assertThrowsInput(-5, "Test for negative input: -5");
}

function test_Check4Prime_checkArgs_above_upper_bound() {
    assertThrowsInput(1001, "Test for upper bound limit: 1001");
}

function test_Check4Prime_checkArgs_char_input() {
    assertThrowsInput('a', "Test for character input: 'a'");
}

function test_Check4Prime_checkArgs_2_inputs() {
    try {
        check4prime.checkArgs(5, 7);
        assert(false, "Test for multiple inputs: 5 and 7");
    } catch (err) {
        assert(true, "Test for multiple inputs: 5 and 7");
    }
}

function test_Check4Prime_checkArgs_empty_input() {
    assertThrowsInput("", "Test for empty input: ''");
}

function test_Check4Prime_checkArgs_undefined_input() {
    assertThrowsInput(undefined, "Test for undefined input");
}

function test_Check4Prime_checkArgs_non_integer_input() {
    assertThrowsInput(3.14, "Test for float input: 3.14");
    assertThrowsInput("12.5", "Test for string float input: '12.5'");
}

/*
Triggered when user submits input via form
*/
function checkFromInput() {
    const input = document.querySelector('input[name="number"]').value;
    document.querySelector('#output').innerHTML = ''; // Clear previous results
    check(input);
}
