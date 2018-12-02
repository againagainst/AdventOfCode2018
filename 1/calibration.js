const stream = input.split(/\s+/).filter(Boolean).map(v => parseInt(v, 10));
const frequencies = {};
let f = 0;

for (let i = 0; true; i++) {
  f = stream.reduce((acc, v) => {
    acc = acc + v;

    if (frequencies[acc]) {
      console.log(`duplicate frequency: ${acc}`);
      process.exit(0);
    } else {
      frequencies[acc] = 1;
    }

    return acc;
  }, f);

  if (i === 0) {
    console.log(`final frequency: ${f}`);
  }
}