

    var slices = [];
    var idCont = 0;

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


function setPrincipal(number) {
    $('div.imgItem').each(function (element) {
        var id = Number($(this).attr('data-imgId'));
        $(this).removeClass('foto-principal')

        if (id == number) {
          var data = JSON.parse($("#data").val());
          data.principal = number;
          $("#data").val(JSON.stringify(data));

          $(this).addClass('foto-principal')
        }
    });
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var image = new Image();
            image.src = e.target.result;

            slices.push({
                src: e.target.result,
                h: image.height,
                w: image.width,
                idCont : idCont
            });

            addImage(e.target.result);


        };

        reader.readAsDataURL(input.files[0]);
    }
}

    function addImage(data, UUID, principal){
      console.log("SLICES", slices);
      $('#fotosGaleria').append('<div class="col-xs-6 col-sd-6 col-md-4 col-lg-3" id="imgItem_' + idCont + '" UUID="'+((UUID)? UUID : "NONE")+'"> <div class="thumbnail imgItem '+((principal)? "foto-principal":"")+'"  data-imgId="' + idCont + '"   ><img class="img-responsive minimun-heigth-miniImg" style="max-width:200px; max-height:150px" onclick="showGallery(this);" src="' + data + '"><hr /><div class="caption"><div class="form-group"><textarea type="text" maxlength="100" class="form-control" on id="titulo_' + idCont + '" value="'+findTituloImageUUID(UUID)+'">'+findTituloImageUUID(UUID)+'</textarea></div><a style="cursor:pointer" class="btn btn-primary" role="button" onClick="setPrincipal(' + idCont + ')" ><span class="glyphicon glyphicon-ok" aria-hidden="true"></span></a><a style="cursor:pointer" class="btn btn-danger" role="button" onClick="removeImage(' + idCont + ')" ><span class="glyphicon glyphicon-trash" aria-hidden="true"></span></a></div></div></div>');

      $('#titulo_'+ idCont).attr("data-ID",idCont).on('input', function() { 
          var data = JSON.parse($("#data").val());
          data.imgsSubir[$(this).attr("data-ID")].titulo = $(this).val();
          $("#data").val(JSON.stringify(data));
      });

      var data = JSON.parse($("#data").val());
      data.imgsSubir[idCont] = {
        UUID : (UUID)? UUID : "NONE",
        titulo : findTituloImageUUID(UUID)
      };
      $("#data").val(JSON.stringify(data));

      if(principal || slices.length === 1)
      {
        setPrincipal(idCont);
      }
      idCont++;

      addButtonUpload();

    }

    function findTituloImageUUID(UUID){
      console.log("Buscando mi titulo", UUID)
      for (var i = 0; i < images.length; i++){

      console.log("¿ESTE?", images[i].UUID, images[i].UUID == UUID)
        if (images[i].UUID == UUID)
        {
          console.log("SI", images[i].UUID, images[i].titulo)
          return images[i].titulo;
        }
           
      }
      return "";
    }

    function removeImage(number){
      var data = JSON.parse($("#data").val());
      delete data.imgsSubir[number];
      $("#data").val(JSON.stringify(data));

      $('#imgItem_'+number).remove();

      removeButtonUpload(number);

      var cont = 0;
      for(; cont < slices.length; cont++)
      {
        if (slices[cont].idCont == number)
          break;
      }
      slices.splice(cont,1);

      if (data.principal == number){
        if (slices.length > 0)
        {
          setPrincipal($('div.imgItem:first').attr("data-imgId"));
        }
      }

    }

    function removeButtonUpload(number){
      $('#upload_'+number).remove();
    }

    function addButtonUpload(){
      $('#etiquetaButton input:last-child').css({ visibility: "collapse" });
      $('#etiquetaButton').append('<input type="file" id="upload_' +idCont + '" name="img_' +idCont + '" onchange="readURL(this);" style="display:none">');
      $('#etiquetaButton').attr("for","upload_" +idCont );
    }

    var FotoPicker = function(nameDiv, imags, principal, title) {

      title = title || "Fotos";


      images = imags;
      console.log(images)
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
          console.log(principal);
          addImage(element.imagen.src,element.UUID,element.UUID === principal);
        }
      });

      init();


      function init(){
        var div = $("#" + nameDiv);
        div.addClass('panel panel-info');
        div.append('<input type="hidden" id="data" name="data" value=\'{ "principal" : -1, "imgsSubir" : {} }\' /><div class="panel-heading">'+title+ '<label for="upload_'+idCont+'" id="etiquetaButton" style="float:right"><span class="glyphicon glyphicon-folder-open" aria-hidden="true" style="font-size: 1.5em"></span><input type="file" id="upload_'+idCont+'" name="img_'+idCont+'" onchange="readURL(this);" style="display:none"></label></div> <div class="panel-body"><div class="row" id="fotosGaleria"> </div></div>')

      }

    }

    FotoPicker.hasPhotos = function() {
      var data = JSON.parse($("#data").val());
      return Object.keys(data.imgsSubir).length > 0;
    }
