import React from 'react'
import Banner from '../components/home/Banner'
import HomeProject from '../components/home/HomeProject'
import Services from '../components/general/Services'
import ContactUs from '../components/home/ContactUs'
import Text from '../components/home/ServicesText'
import Brand from '../components/home/Brand'
import ProjectSlider from '../components/home/ProjectSlider'

export default function Home() {
  return (
    <div>
        <Banner />
        <HomeProject />
        <ContactUs />
        <Text />
        <ProjectSlider />
        <Brand />

    </div>
  )
}
  