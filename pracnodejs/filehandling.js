const fs = require('fs');

fs.writeFile("printing.js","console.log(`async function executed successfully`)",(err)=>{
    if(!result) console.log("File written successfully.");
    else console.log("Error writing file.");
})


