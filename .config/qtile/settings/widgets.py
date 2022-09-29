from libqtile import widget
from settings.theme import colors
# import arcobattery
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=16, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", # Icon: nf-oct-triangle_left
    fontsize=37,
    padding=-3
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=0, padding=50),
    separator(),
]

primary_widgets = [
    *workspaces(),

    powerline('color2', 'dark'),

    icon(bg="color2", fontsize=17, text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
    background=colors['color2'],
    colour_have_updates=colors['text'],
    colour_no_updates=colors['text'],
    no_update_string='0',
    display_format='{updates}',
    update_interval=1800,
    custom_command='checkupdates',
    ),

    powerline('color1', 'color2'),

     icon(bg="color1", fontsize=17, text=' '), # Icon: nf-fa-download

    widget.Memory(**base(bg='color1'), padding=5),

    powerline('color4', 'color1'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download

    widget.CPU(**base(bg='color4'), padding=5),

    # powerline('color3', 'color4'),

    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    # if this dont work change interdace='search in console with ip a. then find pos 2:'
    # widget.Net(**base(bg='color3'), interface='wlp9s0'),

    # arcobattery.BatteryIcon(
    #                     padding=0,
    #                     scale=0.7,
    #                     y_poss=2,
    #                     theme_path="~/.config/qtile/icons/battery_icons_horiz",
    #                     update_interval = 5,
    #                     background = colors[1]
    #                     ),
    # powerline('color2', 'color3'),
    powerline('color2', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '),

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
