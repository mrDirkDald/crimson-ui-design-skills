# Performance-Aware Design

## Perceived performance

Use progressive loading, skeletons only when they mirror real structure, optimistic updates when failure is recoverable, and stable layout to reduce jank.

## Visual cost

Blur, backdrop filters, giant shadows, many translucent layers, large video backgrounds, canvas effects, WebGL, and continuous animation can carry real GPU/battery cost.

## Native cost

Deep view hierarchies, large image decoding, synchronous layout work, and unbounded list rendering can harm responsiveness.

## Lists

Virtualize large collections where appropriate, but preserve keyboard/accessibility behavior and stable scroll anchoring.

## Images

Use correct dimensions/formats, avoid decoding giant originals for tiny thumbnails, and preserve aspect ratio/focal point.
