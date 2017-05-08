

var slices = [];
var idCont = 0;
var principal = "";
function showGallery(element) {
  var pswpElement = document.querySelectorAll('.pswp')[0];

  var mostrar = $(element).parent().attr("data-imgId");

  var index = 0;
  for(; index < slices.length; index++)
  {
    if (slices[index].idCont == mostrar)
      break;
  }

  var options = {
    history: false,
    focus: false,
    showAnimationDuration: 0,
    hideAnimationDuration: 0,
    index : index
  };

  var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, slices, options);
  gallery.init();
}


function addImage(data, UUID, principal){
  console.log(principal);
  $('#fotosGaleria').append('<div class="col-xs-6 col-sd-6 col-md-4 col-lg-3" id="imgItem_' + idCont + '" UUID="'+((UUID)? UUID : "NONE")+'"> <div class="thumbnail imgItem '+((principal)? "foto-principal":"")+'"  data-imgId="' + idCont + '"   ><img class="img-responsive minimun-heigth-miniImg" style="max-width:200px; max-height:150px" onclick="showGallery(this);" src="' + data + '"><hr /><div class="caption"><div class="form-group"><p>'+findTituloImageUUID(UUID)+'</p></div></div></div></div>');

  idCont++;

}

function findTituloImageUUID(UUID){
  for (var i = 0; i < images.length; i++){
    if (images[i].UUID === UUID)
      return images[i].titulo;
  }
  return "";
}

var FotoShower = function(nameDiv, imags, princ, title) {

  title = title || "Fotos";


  images = imags;
  principal = princ;

  images.forEach(function (element,index) {

    element.imagen.onload = function(){
      var height = element.imagen.height;
      var width = element.imagen.width;

      slices.push({
        url: element.imagen.src,
        w: element.imagen.width,
        h: element.imagen.height,
        idCont : idCont
      });
      addImage(element.imagen.src,element.UUID,element.UUID == principal);
    }
  });

  init();


  function init(){
    var div = $("#" + nameDiv);
    div.addClass('panel panel-info');
    div.append('<div class="panel-heading">'+title+ '</div> <div class="panel-body"><div class="row" id="fotosGaleria"> </div></div>')

  }


}
