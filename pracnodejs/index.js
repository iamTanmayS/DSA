const http = require('http');
const fs = require('fs');
const url = require('url')
const express = require('express')
const server = http.createServer((req,res)=>{
        const date = `This web is accessed at ${new Date()} \n ${req.url} \n`
        
        fs.appendFile('info_ip.txt',date,(err,data)=>{
            if (err != null){
            console.log(`we are facing some error, error is ${err}`)}
            else{
                res.end('here is your response')
            }
        })
       
        
})




server.listen(8000,()=>{console.log(`server is running at port`)})