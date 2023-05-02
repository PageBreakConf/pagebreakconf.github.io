window.onload = (event) => {
  // get all the relevant paras
  let paras = document.querySelectorAll("p.speakerlist");
  paras.forEach(function(para) {
    let myText = para.innerHTML;
    myText = myText.replace(/,/g, ", ");
    para.innerHTML = myText;
  });
};