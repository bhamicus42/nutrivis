# import plotly.express as px
import plotly.graph_objects as go
# from plotly.subplots import make_subplots as ms

# https://stackoverflow.com/questions/63713418/offset-polar-bar-radial-origin-python-plotly-express
# https://plotly.com/python/renderers/
# https://plotly.com/python-api-reference/generated/plotly.express.bar_polar.html
#
# fig1 = px.bar_polar(df, r="Amt", theta="Ntrnt",
#                     color="Weight", template="none",
#                     labels={"Amount": "% of RDI"}
#                     )

# fig1 = px.bar_polar(df,
#                     r="Amt",
#                     theta="Ntrnt",
#                     color="Weight",
#                     labels={"Amount": "% of RDI"},
#                     color_discrete_sequence=px.colors.sequential.Plasma_r,
#                     template="plotly_dark")
r_list = [3.5, 1.5, 2.5, 4.5, 4.5, 4, 3]
r_norm = norm = [float(i)/max(r_list) for i in r_list]
r_len = len(r_list)
theta_list = [0] * r_len #[((360)/len(r_list)) * r_list.index(i) for i in r_list]
for i in range(0, r_len):
    theta_list[i] = ((360) / r_len) * i
    print(i, ":  ", theta_list[i])


fig = go.Figure(go.Barpolar(r=r_norm,
                            theta=theta_list, # theta=[0, 60, 120, 180, 240, 300, 350],
                            width=[10, 10, 10, 10, 10, 10, 10],
                            marker_color=["#E4FF87", '#709BFF', '#709BFF', '#FFAA70', '#FFAA70', '#FFDF70', '#B6FFB4'],
                            marker_line_color="black",
                            marker_line_width=2,
                            opacity=0.9))

fig.update_layout(template=None,
                  polar=dict(radialaxis=dict(range=[0, 1],
                                             showticklabels=False,
                                             ticks=''),
                  angularaxis=dict(showticklabels=False,
                                   ticks='')))

# fig.show(renderer="svg")
fig.show()