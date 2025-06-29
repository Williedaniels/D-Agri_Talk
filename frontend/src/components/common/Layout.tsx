
import React, { ReactNode } from 'react';



interface LayoutProps {

  children: ReactNode;

}



function Layout({ children }: LayoutProps) {

  return (

    <div>

      {/* Layout content */}

      {children}

    </div>

  );

}



export default Layout;
