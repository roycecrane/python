vertex_src = """
# version 440
in vec3 pos;
out float tpos;
uniform vec3 Input;
uniform float time;

void main(){
    tpos = pos.z;
    vec2 p_out = time * (pos.xy + vec2(Input.x,-Input.y));
    gl_Position = vec4(-p_out.x, p_out.y, 0.0, 1.0);
}
"""
fragment_src = """
# version 440
in float tpos;
out vec4 out_color;
vec3 lines2(in float val){
    if(val >= 0.0 && val <= 0.1) return vec3(0.2,0.5,0.0);
    if(val >= 0.1 && val <= 0.2) return vec3(0.0,0.2,0.5);
    if(val >= 0.2 && val <= 0.3) return vec3(0.5,0.0,0.2);
    if(val >= 0.3 && val <= 0.4) return vec3(0.2,0.0,0.5);
    if(val >= 0.5 && val <= 0.5) return vec3(0.5,0.2,0.0);
    if(val >= 0.5 && val <= 0.6) return vec3(0.0,0.5,0.2);
    if(val >= 0.6 && val <= 0.7) return vec3(0.4,0.8,0.0);
    if(val >= 0.7 && val <= 0.8) return vec3(0.0,0.4,0.8);
    if(val >= 0.9) return vec3(0.8,0.0,0.4);
}
vec3 lines(in float val){
    if(val >= 100.0/2.0 && val <= 200.0/2.0 ) return vec3(0.0,0.2,0.5);
    if(val >= 200.0/2.0 && val <= 300.0/2.0 ) return vec3(0.5,0.0,0.2);
    if(val >= 300.0/2.0 && val <= 400.0/2.0 ) return vec3(0.2,0.0,0.5);
    if(val >= 500.0/2.0 && val <= 500.0/2.0 ) return vec3(0.5,0.2,0.0);
    if(val >= 500.0/2.0 && val <= 600.0/2.0 ) return vec3(0.0,0.5,0.2);
    if(val >= 600.0/2.0 && val <= 700.0/2.0 ) return vec3(0.4,0.8,0.0);
    if(val >= 700.0/2.0 && val <= 800.0/2.0 ) return vec3(0.0,0.4,0.8);
    if(val >= 900.0/2.0 && val <= 1000.0/2.0 ) return vec3(0.2,0.5,0.0);
    if(val >= 1000) return vec3(0.8,0.0,0.4);
}
void main(){
    vec3 col = lines2(tpos/5.0);
    out_color = vec4(1.0,tpos/1100.0,0.0, 1.0);
}
"""
# fragment_src = """ #version 460
# in vec3 fpos;
# out vec4 out_color;
# float maxIterations = 100;

# vec2 squareImaginary(vec2 number){
# 	return vec2(
# 		pow(number.x,2) - pow(number.y,2), 2*number.x*number.y );
# }
# float iterateMandelbrot(vec2 coord){
# 	vec2 z = vec2(0,0);
# 	for(int i=0;i<maxIterations;i++){
# 		z = squareImaginary(z) + coord;
# 		if(length(z)>2) return i/maxIterations;
# 	}
# 	return maxIterations;
# }
# void main(){
#     float col = 0.0;
#     vec2 p = fpos.xy;
#     col = iterateMandelbrot(p);
#     out_color = vec4(col,0,0,0);
# }"""