var express = require('express');
var request = require('request');
var app = express();
var fs = require('fs');
function excution() {

    // app.use(cors())
    // app.use(bodyParser.json({
    //     limit: '50mb'
    // }));
    // app.use(bodyParser.urlencoded({
    //     limit: '50mb',
    //     extended: true
    // }));
    const headers= require("./input_db.json")

    // app.get('*', (req, res) => {
        console.log('data..')
        var form = {
            data: `{"requestMasterVO":{"sourceId":6,"requestDesc":"Test","requestedEmail":"testFandLName@gmail.com"},
            "descDetailsVO":{"descLarge":"test"},
            "userDetails":{"userFname":${headers.FirstName},"userLname":"testLname"}}`
        }
       console.log(headers.wolken_token) 
       console.log(headers.userEmail)
        //fs.readFile('input_db.json',  function (err, response) {
        //     if (err) throw err;
        // console.log('response!', response);
    //});
    fs.unlink('./TokenValidationCode/final_prg/outpt.json', function (err) {
        if (err) throw err;
    console.log('deleted!');
});
        request({
            headers: {
                'userPsNo': headers.userEmail,
                'wolken_token': headers.wolken_token,
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            uri: 'https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/create_request_generic',
            form:  form,
            method: 'POST'
        }, function (err, res, body) {
            if (err) { 
                console.log("err", err);
                fs.writeFile('outpt.json', body, function (err) {
                    if (err) throw err;
                console.log('Updated!');
            });
                return;
            }else{
                console.log("body", body);

           
                fs.writeFile('./TokenValidationCode/final_prg/outpt.json', body, function (err) {
                    if (err) throw err;
                console.log('Updated!');
                })
            }
           
       
        });
    // })

    return app;
} excution();

// app.listen(process.env.PORT || 8080);
// module.exports = app;

// console.log("your port number:" + config.port);