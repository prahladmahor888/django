document.querySelector('input[type="file"]').addEventListener('change', function(event) { 
    const [file] = event.target.files; 
    if (file) { 
      const reader = new FileReader(); 
      reader.onload = function(e) { 
        const preview = document.getElementById('image-preview'); 
        preview.src = e.target.result; preview.style.display = 'block'; 
      } 
      reader.readAsDataURL(file); 
    } 
  }); 