function frameReady(frame, celImage)
{
  MessageLog.trace("Frame " + frame + " Ready.");
  // Save the image here.
  celImage.imageFile("c:/tmp/myimage" + frame + ".png");
}
function renderFinished()
{
  MessageBox.information("Render Finished");
}
render.renderFinished.connect(renderFinished);
render.frameReady.connect(frameReady);
render.setRenderDisplay("Top/Display");
render.renderSceneAll();
render.renderFinished.disconnect(renderFinished);
render.frameReady.disconnect(frameReady);