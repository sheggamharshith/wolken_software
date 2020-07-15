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

    const headers= require("./input_update.json")
    // app.get('*', (req, res) => {
        console.log('data..')
        var form = {
            data: `{"requestId": ${headers.requestId} , "threadVO": {"resDesc": "Test"}, "otherInfoVO": {"milestoneId": 5}}` // is th e fromat correct..?
        }
  
       console.log(headers.wolken_token) 
       console.log(headers.userPsNo)
        //fs.readFile('input_db.json',  function (err, response) {
        //     if (err) throw err;
        // console.log('response!', response);
    //});
    fs.unlink('./TokenValidationCode/final_prg/output_update.json', function (err) {
        if (err) throw err;
    console.log('deleted!');
});
        request({
            headers: {
                'userPsNo': headers.userPsNo,
                'wolken_token': headers.wolken_token,
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            uri: 'https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/update_request',
            form:  form,
            method: 'POST'
        }, function (err, res, body) {
            if (err) { 
                console.log("err", err);
                fs.writeFile('output_update.json', body, function (err) {
                    if (err) throw err;
                console.log(res.statusCode);
                console.log('it saved an error');
            });
                return;
            }else{
                console.log("body", body);
                console.log(res.statusCode)

           
                fs.writeFile('./TokenValidationCode/final_prg/output_update.json', body, function (err) {
                    if (err) throw err;
                console.log('it saved without error');
                })
            }
           
       
        });
    // })

    return app;
} excution();

// app.listen(process.env.PORT || 8080);
// module.exports = app;

// console.log("your port number:" + config.port);