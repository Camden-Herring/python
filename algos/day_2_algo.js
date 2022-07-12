// var first_name = "camden"

// function reverse_string(str){
//     new_arr = [];
//     for (let i = 0; i<str.length; i++){
//         new_arr[i] = str[i];
//         // console.log(new_arr);
//     }
//     new_arr.reverse();
//     // console.log(new_arr);
//     new_arr.toString();
//     console.log(new_arr);
// }

// reverse_string(first_name)


function reverse_string(str){
  new_str = "";
  for (var i = str.length-1; i>= 0; i--){
    new_str += str[i]
  }
  return new_str
}

console.log(reverse_string("hello world!"))

/* 
//   Acronyms
//   Create a function that, given a string, returns the string’s acronym 
//   (first letter of each word capitalized). 
//   Do it with .split first if you need to, then try to do it without
// */

// const str5 = "object oriented programming";
// const expected5 = "OOP";

// // The 4 pillars of OOP
// const str6 = "abstraction polymorphism inheritance encapsulation";
// const expected6 = "APIE";

// const str7 = "software development life cycle";
// const expected7 = "SDLC";

// // Bonus: ignore extra spaces
// const str8= "  global       information tracker    ";
// const expected8 = "GIT";

// /**
//  * Turns the given str into an acronym.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str A string to be turned into an acronym.
//  * @returns {string} The acronym.
//  */
// var letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

// function acronymize(str) {
//     var prev_char = "";
//     var new_str = ""
//     if (str[0] in "letters"){
//         new_str[0] = str[0]
//         console.log(new_str)
//     }
// }
// // //TEST CODE FOR ACRONYMIZE
// console.log(acronymize(str5)) // Expected: OOP
// console.log(acronymize(str6)) // Expected: APIE
// console.log(acronymize(str7)) // Expected: SDLC
// //BONUS TEST CASE
// console.log(acronymize(str8)) // Expected: GIT
