const CryptoJS = require("crypto-js");


function sW7FumD53pAq3ysvobb(m4Sq1jVkq, ogFjn1FgMP, cFaUNrMEF, prBNGk5) {

    const ktsu = CryptoJS.MD5(m4Sq1jVkq + JSON.stringify(ogFjn1FgMP));

    const dgytI = gAmw9oKGCka50hFH(ktsu, prBNGk5);
    // '"VnXQXzKdNZz3bQ2EMEi8IDwmHtomEbvIy8tbVaogMvPbskJNV52/moSA1XcT9zi27Cl/WHkKksVcDPzUG0BTSQJBMwzvgipNwYZ0hu16LjN2M7qQFxdMKxXWLRJCnultme27EGyZrEZp1wEkxlshrvIqtAAD6sRhl3ZVV2R04Tau3Endj+tNk+RMOObuzFURT9EFkfWkLaga+X2+ri0+RRz1sLCzH4IGHl0rSId6N9EQ26AFUBUeXHPU4Fs09V1FpLw31Ert1xPlpUKuAweiIpHzeP/nTvOQagLDRghQxG1FOnLS/IRrzgc0nJX5qvB4CkdLQvVhzAc="'
    if (!dgytI) {
        var phqbwou = pov0M2gfR(m4Sq1jVkq, ogFjn1FgMP);
        $.ajax({
            url: '../apinew/aqistudyapi.php',
            data: {hXhY1B2Kd: phqbwou},
            type: "post",
            success: function (dgytI) {
                dgytI = deIZLF7oahc0DLiXbqt(dgytI);
                ouK2tR = JSON.parse(dgytI);
                if (ouK2tR.success) {
                    if (prBNGk5 > 0) {
                        ouK2tR.result.time = new Date().getTime(); // 添加当前时间
                        localStorageUtil.save(ktsu, ouK2tR.result);
                    }
                    cFaUNrMEF(ouK2tR.result);
                } else {
                    console.log(ouK2tR.errcode, ouK2tR.errmsg);
                }
            }
        });
    } else {
        cFaUNrMEF(dgytI);
    }
}


function  abc(method, obj) {
    var appId = '271c2aab7dd615dacbadcb41d3c77fa4';
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
    var param = {
        appId: appId,
        method: method,
        timestamp: timestamp,
        clienttype: clienttype,
        object: obj,
        secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
    };
    param = CryptoJS.enc.Base64.encrypt(JSON.stringify(param));
    //dckE15Yk15AF : oHLKvpN54hwpLWjt
    //dcik4kPiOWjo : pdgLk9FGBd5kXbm0
    param = DES.encrypt(param, dckE15Yk15AF, dcik4kPiOWjo);
    return param;
}

//DES

function desencrypt( text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.encrypt(text, secretkey, {
        iv: secretiv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
}
function desdecrypt(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.decrypt(text, secretkey, {
        iv: secretiv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
}

//  AES
function aesencrypt(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    // console.log('real key:', secretkey);
    // console.log('real iv:', secretiv);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.encrypt(text, secretkey, {
        iv: secretiv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
}
// DES

function aesDES(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.decrypt(text, secretkey, {
        iv: secretiv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
}


function Base64() {
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    this.encode = function(a) {
        var c, d, e, f, g, h, i, b = "", j = 0;
        for (a = _utf8_encode(a); j < a.length; )
            c = a.charCodeAt(j++),
                d = a.charCodeAt(j++),
                e = a.charCodeAt(j++),
                f = c >> 2,
                g = (3 & c) << 4 | d >> 4,
                h = (15 & d) << 2 | e >> 6,
                i = 63 & e,
                isNaN(d) ? h = i = 64 : isNaN(e) && (i = 64),
                b = b + _keyStr.charAt(f) + _keyStr.charAt(g) + _keyStr.charAt(h) + _keyStr.charAt(i);
        return b
    }
    ;
    this.encrypt = function(text) {
        return this.encode(text);
    };
    this.decrypt =  function(text) {
        return this.decode(text);
    }
    this.decode = function(a) {
        var c, d, e, f, g, h, i, b = "", j = 0;
        for (a = a.replace(/[^A-Za-z0-9\+\/\=]/g, ""); j < a.length; )
            f = _keyStr.indexOf(a.charAt(j++)),
                g = _keyStr.indexOf(a.charAt(j++)),
                h = _keyStr.indexOf(a.charAt(j++)),
                i = _keyStr.indexOf(a.charAt(j++)),
                c = f << 2 | g >> 4,
                d = (15 & g) << 4 | h >> 2,
                e = (3 & h) << 6 | i,
                b += String.fromCharCode(c),
            64 != h && (b += String.fromCharCode(d)),
            64 != i && (b += String.fromCharCode(e));
        return b = _utf8_decode(b)
    }
    ;
    _utf8_encode = function(a) {
        var b, c, d;
        for (a = a.replace(/\r\n/g, "\n"),
                 b = "",
                 c = 0; c < a.length; c++)
            d = a.charCodeAt(c),
                128 > d ? b += String.fromCharCode(d) : d > 127 && 2048 > d ? (b += String.fromCharCode(192 | d >> 6),
                    b += String.fromCharCode(128 | 63 & d)) : (b += String.fromCharCode(224 | d >> 12),
                    b += String.fromCharCode(128 | 63 & d >> 6),
                    b += String.fromCharCode(128 | 63 & d));
        return b
    }
    ;
    _utf8_decode = function(utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
        while (i < utftext.length) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++
            } else {
                if ((c > 191) && (c < 224)) {
                    c2 = utftext.charCodeAt(i + 1);
                    string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                    i += 2
                } else {
                    c2 = utftext.charCodeAt(i + 1);
                    c3 = utftext.charCodeAt(i + 2);
                    string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                    i += 3
                }
            }
        }
        return string
    }
}
function base64decry(text) {
    const  base64constant= new Base64();
    return base64constant.decode(text);
}

function hex_md5(data) {
    return CryptoJS.MD5(data).toString()
}
function str2rstr_utf8(input) {
    var output = "";
    var i = -1;
    var x, y;
    while (++i < input.length) {
        x = input.charCodeAt(i);
        y = i + 1 < input.length ? input.charCodeAt(i + 1) : 0;
        if (0xD800 <= x && x <= 0xDBFF && 0xDC00 <= y && y <= 0xDFFF) {
            x = 0x10000 + ((x & 0x03FF) << 10) + (y & 0x03FF);
            i++
        }
        if (x <= 0x7F)
            output += String.fromCharCode(x);
        else if (x <= 0x7FF)
            output += String.fromCharCode(0xC0 | ((x >>> 6) & 0x1F), 0x80 | (x & 0x3F));
        else if (x <= 0xFFFF)
            output += String.fromCharCode(0xE0 | ((x >>> 12) & 0x0F), 0x80 | ((x >>> 6) & 0x3F), 0x80 | (x & 0x3F));
        else if (x <= 0x1FFFFF)
            output += String.fromCharCode(0xF0 | ((x >>> 18) & 0x07), 0x80 | ((x >>> 12) & 0x3F), 0x80 | ((x >>> 6) & 0x3F), 0x80 | (x & 0x3F))
    }
    return output
}
function poPBVxzNuafY8Yu(m0fhOhhGL, oNLhNQ){
    oNLhNQ={
        'city': oNLhNQ
    }
    var aMFs = '3c9208efcfb2f5b843eec8d96de6d48a';
    var cVWG2 = 'WEB';
    const acky6QolJSJi='dLRSzDrm8xkryEyL'
    const acixHVhiNqmK='fex6AA4zRfVrSPmr'
    var t5GECZQ = '1731860388838';
    const  base64constant= new Base64();
    var pKmSFk8 = {
        appId: aMFs,
        method: m0fhOhhGL,
        timestamp: t5GECZQ,
        clienttype: cVWG2,
        object: oNLhNQ,
        secret: hex_md5(aMFs + m0fhOhhGL + t5GECZQ + cVWG2 + JSON.stringify(osZ34YC04S(oNLhNQ)))
    };
    pKmSFk8 = base64constant.encrypt(JSON.stringify(pKmSFk8));
    pKmSFk8 = aesencrypt(pKmSFk8, acky6QolJSJi, acixHVhiNqmK);
    return pKmSFk8;
};

function osZ34YC04S(obj){
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
        newObject[key] = obj[key];
    });
    return newObject;
}
function sSPnfjolBsGjl66hUEw8(m0fhOhhGL, oBDNNVgaDf, cCLupMFJ7, p5kr85Z) {
    // const k1pT = hex_md5(m0fhOhhGL + JSON.stringify(oBDNNVgaDf));

    // const dGHdO = golmOACJkTUULBcU(k1pT, p5kr85Z);
    // if (!dGHdO) {
        var pKmSFk8 = poPBVxzNuafY8Yu(m0fhOhhGL, oBDNNVgaDf);
        return pKmSFk8;

}



console.log(poPBVxzNuafY8Yu('GETMONTHDATA','杭州'))