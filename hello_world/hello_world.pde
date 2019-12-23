//si gris, on peut ne donner qu'une value.
//size(1280,750); // full size
size(500,300);
//background(230);
background(#E6E6E6);
smooth();
int radius=70;
int halfw = width/2;
int halfh = height/2;
//stroke(130,0,0,100);// on peut mettre de la alpha value sur le stroke
stroke(130,0,0);
strokeWeight(4);
//noStroke(); // pour désactiver le trait
line(halfw-radius,halfh-radius,halfw+radius,halfh+radius);
line(halfw+radius,halfh-radius,halfw-radius,halfh+radius);
fill(255,150);
//noFill(); // pour desactiver le remplissage
int circle_radius=50;
ellipse(halfw,halfh,circle_radius,circle_radius);
