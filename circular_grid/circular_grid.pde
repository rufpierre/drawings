int ite=50;

float posit(float pos){
  int zoom=width/2;
  int trans=zoom;
  return trans+zoom*pos;
}

float circx(int i){
  return cos(2*PI*i/ite);
}

float circy(int i){
  return sin(2*PI*i/ite);
}

void setup(){
  size(700,700);
  background(80,60,50);
  //background(50);
  //smooth();
    for (int i=0;i<ite;i++){
    for(int j=0;j<ite;j++){
      /*if(j<18){
        stroke((i*256/ite)%256,256-((i*256/ite)%256),128,1.5*(256-((i*256/ite)%256)));
        strokeWeight(1);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }
      if(j<8){
        stroke(0);
        strokeWeight(1);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }
      if(j>8 && j<12){
        stroke(128,100);
        strokeWeight(2);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }
      if(j>2 && j<12){
        stroke(0,0,150,100);
        strokeWeight(2);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }*/
      for (int k=0;k<0.55*ite;k=k+2){
        if(j<k){
          //stroke((1*256/ite)%256,255);
          float ind=(1.4*pow(k,0.498)*256/pow(ite,0.5));
          float coef = 0.89;
          stroke(1.5*ind*coef,1*ind*coef,1.5*ind*coef,256-0.9*ind);
          //stroke(0,256-(pow(k/ite,1)*256));
          strokeWeight(1);
          line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
        }      
      }

/*
      if(j<10){
        //stroke((1*256/ite)%256,255);
        stroke(0,255);
        strokeWeight(1);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }      

      if(j<12){
        //stroke((7*256/ite)%256,100);
        stroke(0,150);
        strokeWeight(1);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }      

      if(j<15){
        //stroke((15*256/ite)%256,15);
        stroke(0,15);
        strokeWeight(1);
        line(posit(circx(i)),posit(circy(i)),posit(circx(i+j)),posit(circy(i+j)));
      }      
  */
}
  }
}
