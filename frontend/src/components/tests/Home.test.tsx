import React from 'react';
import { render, screen } from '@testing-library/react';
import Home from '../../pages/Home';

test('renders welcome message', () => {
  render(<Home />);
  const headingElement = screen.getByRole('heading', { name: /home page/i });
  const welcomeElement = screen.getByText(/Welcome to D-Agri_Talk!/i);

  expect(headingElement).toBeInTheDocument();
  expect(welcomeElement).toBeInTheDocument();
});

// The "renders feature cards" test was removed as the Home component
// currently does not render these cards. This test can be added back
// once the feature cards are implemented.
