// src/components/Sidebar.js
import React from 'react';
import { Drawer, List, ListItem, ListItemIcon, ListItemText, Divider } from '@mui/material';
import { People, Group, EventNote, QuestionAnswer, Notes, Notifications, Assessment, AdminPanelSettings, Search } from '@mui/icons-material';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: 240,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: 240,
          boxSizing: 'border-box',
        },
      }}
    >
      <List>
        <ListItem button component={Link} to="/user-management">
          <ListItemIcon><People /></ListItemIcon>
          <ListItemText primary="User Management" />
        </ListItem>

        <ListItem button component={Link} to="/team-management">
          <ListItemIcon><Group /></ListItemIcon>
          <ListItemText primary="Team Management" />
        </ListItem>

        <ListItem button component={Link} to="/interview-scheduling">
          <ListItemIcon><EventNote /></ListItemIcon>
          <ListItemText primary="Interview Scheduling" />
        </ListItem>

        <ListItem button component={Link} to="/question-repository">
          <ListItemIcon><QuestionAnswer /></ListItemIcon>
          <ListItemText primary="Question Repository" />
        </ListItem>

        <ListItem button component={Link} to="/mom">
          <ListItemIcon><Notes /></ListItemIcon>
          <ListItemText primary="Minutes of Meeting" />
        </ListItem>

        <ListItem button component={Link} to="/notifications">
          <ListItemIcon><Notifications /></ListItemIcon>
          <ListItemText primary="Notifications & Reminders" />
        </ListItem>

        <ListItem button component={Link} to="/reporting">
          <ListItemIcon><Assessment /></ListItemIcon>
          <ListItemText primary="Reports & Analytics" />
        </ListItem>

        <Divider />

        <ListItem button component={Link} to="/admin-panel">
          <ListItemIcon><AdminPanelSettings /></ListItemIcon>
          <ListItemText primary="Admin Panel" />
        </ListItem>

        <ListItem button component={Link} to="/search">
          <ListItemIcon><Search /></ListItemIcon>
          <ListItemText primary="Search" />
        </ListItem>

        <ListItem button component={Link} to="/user-login">
          <ListItemIcon><AdminPanelSettings /></ListItemIcon>
          <ListItemText primary="Login" />
        </ListItem>

        <ListItem button component={Link} to="/user-register">
          <ListItemIcon><AdminPanelSettings /></ListItemIcon>
          <ListItemText primary="UserRegister" />
        </ListItem>
      </List>
    </Drawer>
  );
};

export default Sidebar;
