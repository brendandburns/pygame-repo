import 'skulpt'
import 'skulpt-pygame-zero'

import pythonCode from './game.py'

function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
          throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function output(text) {
  var pre = document.getElementById("output");
  pre.innerHTML = pre.innerHTML + `<pre>${text}</pre>`;
}

function exceptionHandler(err) {
  console.log(err.nativeError);
  var pre = document.getElementById("output");
  pre.innerHTML = pre.innerHTML + err;
}

function start() {
  var pre = document.getElementById("output");
  pre.innerHTML = "";
  Sk.pre = "output";

  Sk.configure({
    output: output,
    read: PyGameZero.usePyGameZero(builtinRead),
    uncaughtException: exceptionHandler,
    __future__: Sk.python3,
  });

  PyGameZero.setContainer(document.getElementById('stage'));

  // insert before running
  PyGameZero.reset();
  // running skulpt
  var promise = Sk.misceval.asyncToPromise(function() {
	  return Sk.importMainWithBody("<stdin>", false, pythonCode, true);
  });

  promise.then(
    () => {
      console.log("success"),
      document.getElementById("loading").innerHTML = "";
    },
    exceptionHandler,
  );
}

start();