var sendComment = function()
{
  console.log("Comment sending function.");
  var xmlhttp;    
  
  lessonId = "LessonId";
  content = "Comment";
  target = "/comment/create/";
  if (! content)
    {
    alert("Empty comment.");
    return;
    }
  if (!lessonId) {
    alert("Empty lessonId");
    return;
  }
  
  $.ajax({
    method: "POST",
    url: "",
    data: { lessonId: lessonId, content: content},
    timeout: 2.0,
    success: function() {
      alert("success");
    }
    .done (function() {
      alert("Ajax sent.");
    })
    .fail(function() {
      alert("Failed");
    })
  });
}

var uploadFile = function() {
  var file = $("#fileUpload")[0].files[0];
  formData = new FormData();
  formData.append('file', file);

  $.ajax('/meterial/create/', {
    method: 'POST',
    contentType: false,
    processData: false,
    data: formData
  });
}

window.onload = function() {
  initChart();
  initForm();
}


var initChart = function() {
  var ctx_average = $("#chart-average").get(0).getContext("2d");
  window.myLine = new Chart(ctx_average).Line(lineChartData, {
    responsive: false
  });
  var ctx_distribution = $("#chart-distribution").get(0).getContext("2d");
  window.myPie = new Chart(ctx_distribution).Pie(pieData, {
    responsive: false
  });
}

var initForm = function() {
  var form = $("#fileUploadForm")[0];
  var file = $("#fileUpload")[0].files[0];
  var uploadButton = $("#fileUploadButton")[0];

  form.onsubmit = function(event) {
    event.preventDefault();

    // Update button text.
    uploadButton.innerHTML = 'Uploading...';
    uploadButton.disabled = true;

    var formData = new FormData();
    formData.append("lessonID", lessonId);
    //formData.append("title", file.name);
    formData.append('file', file);
  
    $.ajax('/meterial/create/', {
      method: 'POST',
      contentType: false,
      processData: false,
      data: formData,
      timeout: 2.0,
      success: function() {
        uploadButton.InnerHTML = "上传";
        uploadButton.disabled = false;
        alert("上传完成");
      },
      fail: function() {
        uploadButton.InnerHTML = "上传";
        uploadButton.disabled = false;
        alert("上传失败");
      }
    });
  }
}