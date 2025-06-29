import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders home page on initial load', () => {
  render(<App />);
  const headingElement = screen.getByRole('heading', { name: /home page/i });
  expect(headingElement).toBeInTheDocument();
});
