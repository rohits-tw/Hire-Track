// src/components/HomePage.js
import React from 'react';
import { Box, Button, Container, Grid, Paper, Typography } from '@mui/material';
import { People, Group, EventNote, QuestionAnswer, Assessment } from '@mui/icons-material';

const HomePage = () => {
  return (
    <Container>
      <Typography variant="h4" sx={{ mt: 3, mb: 3 }}>Welcome to HireTrack</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <People fontSize="large" />
            <Typography variant="h6" sx={{ mt: 2 }}>User Management</Typography>
            <Typography variant="body1">Manage user registrations, profiles, and roles.</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Group fontSize="large" />
            <Typography variant="h6" sx={{ mt: 2 }}>Team Management</Typography>
            <Typography variant="body1">Create teams and assign users to technical teams.</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <EventNote fontSize="large" />
            <Typography variant="h6" sx={{ mt: 2 }}>Interview Scheduling</Typography>
            <Typography variant="body1">Schedule and track interviews with detailed statuses.</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <QuestionAnswer fontSize="large" />
            <Typography variant="h6" sx={{ mt: 2 }}>Question Repository</Typography>
            <Typography variant="body1">Manage and categorize interview questions.</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Assessment fontSize="large" />
            <Typography variant="h6" sx={{ mt: 2 }}>Reports & Analytics</Typography>
            <Typography variant="body1">Analyze interview metrics and trends.</Typography>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default HomePage;
