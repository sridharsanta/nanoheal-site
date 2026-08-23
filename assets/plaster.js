// Warm carved-plaster texture behind the hero card — echoes the reference site's
// relief photography without shipping an image.
(function(){
  var c = document.getElementById('plaster');
  if(!c) return;
  var ctx = c.getContext('2d'), w, h;
  function dark(){
    var t = document.documentElement.getAttribute('data-theme');
    if(t === 'dark') return true;
    if(t === 'light') return false;
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function draw(){
    w = c.width = c.offsetWidth; h = c.height = c.offsetHeight;
    if(!w || !h) return;
    var d = dark();
    ctx.fillStyle = d ? '#1C1918' : '#E4E1DF';
    ctx.fillRect(0,0,w,h);
    var img = ctx.getImageData(0,0,w,h), p = img.data;
    // low-frequency value noise -> relief-like banding
    var g = 46, grid = [];
    for(var i=0;i<(g+1)*(g+1);i++) grid.push(Math.random());
    function val(x,y){
      // tile the sample space so higher octaves can never index past the grid
      x = x - Math.floor(x); y = y - Math.floor(y);
      var gx = x*g, gy = y*g, x0 = gx|0, y0 = gy|0;
      if(x0 >= g) x0 = g-1; if(y0 >= g) y0 = g-1;
      var fx = gx-x0, fy = gy-y0;
      var sx = fx*fx*(3-2*fx), sy = fy*fy*(3-2*fy);
      var a = grid[y0*(g+1)+x0], b = grid[y0*(g+1)+x0+1];
      var cc = grid[(y0+1)*(g+1)+x0], dd = grid[(y0+1)*(g+1)+x0+1];
      return (a+(b-a)*sx) + ((cc+(dd-cc)*sx) - (a+(b-a)*sx))*sy;
    }
    for(var y=0;y<h;y++){
      for(var x=0;x<w;x++){
        var n = val(x/w, y/h)*1.0 + val(x/w*2.3, y/h*2.3)*0.5;
        // contour the field so it reads as carved ridges, then soften
        var ridge = Math.abs(Math.sin(n*7.0));
        var v = (ridge*0.55 + n*0.25);
        var amt = d ? v*26 - 8 : v*30 - 12;
        var k = (y*w+x)*4;
        p[k] += amt; p[k+1] += amt*0.96; p[k+2] += amt*0.9;
      }
    }
    ctx.putImageData(img,0,0);
    // soften the left edge into the panel
    var grd = ctx.createLinearGradient(0,0,w*0.5,0);
    grd.addColorStop(0, d ? 'rgba(28,25,24,.85)' : 'rgba(228,225,223,.85)');
    grd.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = grd; ctx.fillRect(0,0,w,h);
  }
  var t; function go(){ clearTimeout(t); t = setTimeout(draw, 120); }
  draw(); window.addEventListener('resize', go);
  var mq = window.matchMedia('(prefers-color-scheme: dark)');
  (mq.addEventListener ? mq.addEventListener('change', go) : mq.addListener(go));
})();
