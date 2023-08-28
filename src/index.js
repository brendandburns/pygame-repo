import 'skulpt'
import 'skulpt-pygame-zero'

import pythonCode from './game.py'

function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
          throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function component() {
  const element = document.createElement('div');

  // Lodash, currently included via a script, is required for this line to work
  // element.innerHTML = _.join(['Hello', 'webpack'], ' ');

  Sk.configure({
    read: PyGameZero.usePyGameZero(builtinRead),
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
    () => console.log("success"),
    (err) => {
      console.log(err.nativeError);
      var mypre = document.getElementById("output");
      mypre.innerHTML = mypre.innerHTML + err;
    }
  );

  return element;
}

document.body.appendChild(component());
