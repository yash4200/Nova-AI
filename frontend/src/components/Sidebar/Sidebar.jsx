import "./Sidebar.css";

import {

Home,

Mic,

BarChart3,

FileText,

CloudSun,

Settings

} from "lucide-react";

function Sidebar(){

return(

<div className="sidebar">

<h1>NOVA</h1>

<ul>

<li><Home size={20}/> Dashboard</li>

<li><Mic size={20}/> Voice</li>

<li><CloudSun size={20}/> Weather</li>

<li><BarChart3 size={20}/> Analysis</li>

<li><FileText size={20}/> Reports</li>

<li><Settings size={20}/> Settings</li>

</ul>

</div>

)

}

export default Sidebar;