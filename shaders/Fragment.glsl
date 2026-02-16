#version 410 core

layout(location =0) out vec4 fragment_colour;
in vec3 out_colour;
void main()
{
    vec2 circle_cord = 2.0 * gl_PointCoord - 1.0;
    if(dot(circle_cord,circle_cord) > 1.0)
    {
        discard;
    }

    ////  Super Glowing Alpha Process, Getting Flash Outline
    float glow = exp(dot(circle_cord,circle_cord) * 2.0);
    float edge = smoothstep(1.0, 0.6, sqrt(dot(circle_cord,circle_cord)));

    vec3 color = out_colour * (0.2 + glow);
    float alpha = glow * edge;

    fragment_colour = vec4(color, alpha);

}
