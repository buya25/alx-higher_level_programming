## alx-higher_level_programming: 0x12-javascript-warm_up

### 0. First constant, first print
```bash
#!/usr/bin/node
const myVar = "JavaScript is amazing";
console.log(myVar);
```

### 1. 3 languages
```bash
#!/usr/bin/node
console.log("C is fun");
console.log("Python is cool");
console.log("JavaScript is amazing");
```

### 2. Arguments
```bash
#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
```

### 3. Value of my argument
```bash
#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
```

### 4. Create a sentence
```bash
#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(arg1 + ' is ' + arg2);
```

### 5. An Integer
```bash
#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
```

### 6. Loop to languages
```bash
#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const language of languages) {
  console.log(language);
}
```

### 7. I love C
```bash
#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
```

### 8. Square
```bash
#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
```

### 9. Add
```bash
#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add(a, b) {
  return a + b;
}

console.log(add(a, b));
```

### 10. Factorial
```bash
#!/usr/bin/node
function factorial(n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));
```

### 11. Second biggest!
```bash
#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => a - b);
  console.log(sortedArgs[sortedArgs.length - 2]);
}
```

### 12. Object
```bash
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.value = 89;

console.log(myObject);
```

### 13. Add file
```javascript
// 13-add.js
#!/usr/bin/node
exports.add = function add(a, b) {
  return a + b;
};
```

```bash
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
```

### 14. Const or not const
```javascript
// 100-let_me_const.js
#!/usr/bin/node
myVar = 333;
```

```bash
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const');
console.log(myVar);
```

### 15. Call me Moby
```javascript
// 101-call_me_moby.js
#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
```

```bash
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
```

### 16. Add me maybe
```javascript
// 102-add_me_maybe.js
#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
```

```bash
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
```

### 17. Increment object
```javascript
// 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
```

```bash
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
